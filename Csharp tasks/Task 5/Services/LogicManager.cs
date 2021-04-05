using Microsoft.AspNetCore.Cryptography.KeyDerivation;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Claims;
using System.Security.Cryptography;
using System.Threading.Tasks;
using Task_5.Models;

namespace Task_5.Services
{
    public class LogicManager : ILogicManager
    {
        private DataBaseContext DBContext = new DataBaseContext();

        public LogicManager(DataBaseContext ctx)
        {
            DBContext = ctx;
        }
        
        public (List<Order> res, int count) Index(string s, string sort_by, string sort_order, int offset, int limit)
        {
            List<Order> list_of_orders = new List<Order>();
            if (s != null)
                list_of_orders = Search(DBContext.Orders.ToList(), s);
            else
                list_of_orders = DBContext.Orders.ToList();

            list_of_orders = Sort(list_of_orders, sort_order, sort_by);

            if (limit == null || limit < 1)
            {
                limit = list_of_orders.Count;
            }
            if (offset == null || offset < 1)
                offset = 1;
            List<Order> to_return = Paginate(list_of_orders, offset, limit);
            return (to_return, list_of_orders.Count);
        }

        public int Create_new_order(Order to_add)
        {
            try
            {
                DBContext.Orders.Add(to_add);
                DBContext.SaveChanges();
                return 201;
            }
            catch
            {
                return 401;
            }
        }

        public (int status, Order res) Delete_order(int id)
        {
            Order to_remove = DBContext.Orders.FirstOrDefault(order => order.Id == id);
            if (to_remove is null)
                return (404, null);
            DBContext.Orders.Remove(to_remove);
            DBContext.SaveChanges();
            return (202, to_remove);
        }

        public Order Get_one_order(int id)
        {
            Order to_show = DBContext.Orders.FirstOrDefault(order => order.Id == id);
            if (to_show is null)
                return null;
            return to_show;
        }

        public int Edit_order(int id, Order new_order)
        {
            Order to_edit = DBContext.Orders.FirstOrDefault(order => order.Id == id);
            if (to_edit is null)
                return 404;
            try
            {
                foreach (var prop in to_edit.GetType().GetProperties())
                {
                    prop.SetValue(to_edit, new_order.GetType().GetProperty(prop.Name).GetValue(new_order));
                }
                DBContext.Orders.Update(to_edit);
                DBContext.SaveChanges();
                return 203;
            }
            catch
            {
                return 401;
            }
        }
        private List<Order> Search(List<Order> coll, string search_data)
        {
            bool added = false;
            List<Order> res = new List<Order>();
            foreach (var order in coll)
            {
                foreach (var prop in order.GetType().GetProperties())
                {
                    if (prop.GetValue(order).ToString().ToLower().Contains(search_data.ToLower())
                        && !added)
                    {
                        res.Add(order);
                        added = true;
                    }
                }
                added = false;
            }
            return res;
        }
        private List<Order> Paginate(List<Order> coll, int page_num, int page_size)
        {
            List<Order> res = coll.Skip((page_num - 1) * page_size).Take(page_size).ToList();
            return res;
        }
        private List<Order> Sort(List<Order> coll, string sort_direction, string sort_by_this)
        {
            foreach (var prop in typeof(Order).GetProperties())
            {
                if (prop.Name == sort_by_this && sort_direction == "desc")
                {
                    coll = coll.OrderByDescending(c => c.GetType().GetProperty(sort_by_this).GetValue(c, null)).ToList();
                    return coll;
                }
                if (prop.Name == sort_by_this)
                {
                    coll = coll.OrderBy(c => c.GetType().GetProperty(sort_by_this).GetValue(c, null)).ToList();
                    return coll;
                }
            }
            return coll;
        }


        public ClaimsIdentity GetIdentity(string username, string password)
        {
            var person = DBContext.Users.FirstOrDefault(u => u.Login == username);
            
            if (person != null)
            {
                /* Fetch the stored value */
                string savedPasswordHash = person.Password;
                /* Extract the bytes */
                byte[] hashBytes = Convert.FromBase64String(savedPasswordHash);
                /* Get the salt */
                byte[] salt = new byte[16];
                Array.Copy(hashBytes, 0, salt, 0, 16);
                /* Compute the hash on the password the user entered */
                var pbkdf2 = new Rfc2898DeriveBytes(password, salt, 100000);
                byte[] hash = pbkdf2.GetBytes(20);
                /* Compare the results */
                for (int i = 0; i < 20; i++)
                    if (hashBytes[i + 16] != hash[i])
                        return null;

                var claims = new List<Claim>
                {
                    new Claim(ClaimsIdentity.DefaultNameClaimType, person.Login),
                    new Claim(ClaimsIdentity.DefaultRoleClaimType, person.Role)
                };
                ClaimsIdentity claimsIdentity =
                new ClaimsIdentity(claims, "Token", ClaimsIdentity.DefaultNameClaimType,
                                    ClaimsIdentity.DefaultRoleClaimType);
                return claimsIdentity;
            }
            return null;
        }

        public List<Order> Get_my_orders(string username)
        {
            var list_of_orders = DBContext.Orders.ToList();
            List<Order> my_orders = new List<Order>();
            foreach (var order in list_of_orders)
            {
                if(order.Customer_email == username)
                {
                    my_orders.Add(order);
                }

            }
            return my_orders;
        }

        public Order Get_my_one_order(string username, int id)
        {
            Order getbyid = DBContext.Orders.FirstOrDefault(order => order.Id == id);
            if (getbyid.Customer_email == username)
                return getbyid;
            return null;
        }

        public Product ChangeProductAmount(int productId, int new_amount)
        {
            Product res = DBContext.Products.FirstOrDefault(x => x.Id == productId);
            Product newProd = new Product
            {
                Id = res.Id,
                Amount = new_amount
            };
            try
            {
                DBContext.Products.Remove(res);
                DBContext.Products.Add(newProd);
                DBContext.SaveChanges();
                return newProd;
            }
            catch
            {
                return null;
            }
        }
        public int GetProductAmount(int productId)
        {
            Product res = DBContext.Products.FirstOrDefault(x => x.Id == productId);
            return res.Amount;
        }

        public Order Create_my_order(string username, PersonalOrderCreationData order_data)
        {
            Order to_add = new Order()
            {
                Order_status = "not paid",
                Amount = order_data.Amount,
                Discount = 0,
                Order_date = DateTime.Now,
                Shipped_date = order_data.Shipped_date,
                Customer_email = username,
                ProductId = order_data.ProductId 
            };
            Product product = DBContext.Products.FirstOrDefault(x => x.Id == to_add.ProductId);
            try
            {
                if (product.Amount < to_add.Amount)
                    return null;
                product.Amount -= to_add.Amount;
                DBContext.Products.Update(product);
                DBContext.Orders.Add(to_add);
                DBContext.SaveChanges();;
                return to_add;
            }
            catch
            {
                return null;
            }
        }
        
        public Person AddUser(string username, string password)
        {
            Person new_user = new Person
            {
                Login = username,
                Password = HashPassword(password),
                Role = "user"
            };
            try
            {
                DBContext.Users.Add(new_user);
                DBContext.SaveChanges();
                return new_user;
            }
            catch
            {
                return null;
            }
        }

        public Product DeleteProduct(int id)
        {
            Product res = DBContext.Products.FirstOrDefault(x => x.Id == id);
            if(res != null)
            {
                DBContext.Products.Remove(res);
                DBContext.SaveChanges();
                return res;
            }
            return null;
        }

        public Product AddProduct(int id, int amount)
        {
            Product to_add = new Product
            {
                Id = id,
                Amount = amount
            };
            try
            {
                DBContext.Products.Add(to_add);
                DBContext.SaveChanges();
                return to_add;
            }
            catch
            {
                return null;
            }
        }
        public static string HashPassword(string password)
        {
            byte[] salt;
            new RNGCryptoServiceProvider().GetBytes(salt = new byte[16]);
            //STEP 2 Create the Rfc2898DeriveBytes and get the hash value:

            var pbkdf2 = new Rfc2898DeriveBytes(password, salt, 100000);
            byte[] hash = pbkdf2.GetBytes(20);
            //STEP 3 Combine the salt and password bytes for later use:

            byte[] hashBytes = new byte[36];
            Array.Copy(salt, 0, hashBytes, 0, 16);
            Array.Copy(hash, 0, hashBytes, 16, 20);

            //STEP 4 Turn the combined salt+hash into a string for storage
            string savedPasswordHash = Convert.ToBase64String(hashBytes);
            return savedPasswordHash;
        }

    }
}
