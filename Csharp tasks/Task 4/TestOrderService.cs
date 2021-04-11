using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Task_4.Services;

namespace Task_4.Tests
{
    class TestOrderService : ILogicManager
    {
        private readonly List<Order> orders;
        public TestOrderService()
        {
            orders = new List<Order>()
            {
                new Order
                {
                    Id = 1,
                    Order_status = "paid",
                    Amount = 10,
                    Discount = 50,
                    Order_date = new DateTime(2020, 5, 6),
                    Shipped_date = new DateTime(2020, 5, 13),
                    Customer_email = "email1@gmail.com"
                },
                new Order
                {
                    Id = 2,
                    Order_status = "not paid",
                    Amount = 20,
                    Discount = 10,
                    Order_date = new DateTime(2020, 10, 6),
                    Shipped_date = new DateTime(2020, 11, 6),
                    Customer_email = "email2@gmail.com"
                },
                new Order
                {
                    Id = 3,
                    Order_status = "not paid",
                    Amount = 1,
                    Discount = 0,
                    Order_date = new DateTime(2020, 5, 6),
                    Shipped_date = new DateTime(2020, 5, 13),
                    Customer_email = "email3@gmail.com"
                },
                new Order
                {
                    Id = 4,
                    Order_status = "not paid",
                    Amount = 2,
                    Discount = 15,
                    Order_date = new DateTime(2021, 3, 22),
                    Shipped_date = new DateTime(2021, 3, 29),
                    Customer_email = "email4@gmail.com"
                },
                new Order
                {
                    Id = 5,
                    Order_status = "refunded",
                    Amount = 500,
                    Discount = 30,
                    Order_date = new DateTime(2011, 1, 1),
                    Shipped_date = new DateTime(2011, 1, 1),
                    Customer_email = "email5@gmail.com"
                },
                new Order
                {
                    Id = 6,
                    Order_status = "paid",
                    Amount = 100,
                    Discount = 0,
                    Order_date = new DateTime(2010, 2, 2),
                    Shipped_date = new DateTime(2011, 2, 2),
                    Customer_email = "email6@gmail.com"
                }
            };
        }

        public (List<Order> res, int count) Index(string s, string sort_by, string sort_order, int offset=0, int limit=0)
        {
            List<Order> list_of_orders = new List<Order>();
            if (s != null)
                list_of_orders = Search(orders, s);
            else
                list_of_orders = orders;

            list_of_orders = Sort(list_of_orders, sort_order, sort_by);

            if (limit == null || limit < 1)
            {
                limit = list_of_orders.Count;
            }
            if (offset == null || offset < 1)
                offset = 1;
            List<Order> to_return = Paginate(list_of_orders, offset, limit);
            return (to_return, to_return.Count);
        }
        public int Create_new_order(Order to_add)
        {
            if(Check_id(to_add, orders))
            {
                orders.Add(to_add);
                return 201;
            }
            return 401;
        }
        public (int status, Order res) Delete_order(int id)
        {
            Order to_remove = orders.FirstOrDefault(order => order.Id == id);
            if (to_remove is null)
                return (404, null);
            orders.Remove(to_remove);
            return (202, to_remove);
        }
        public Order Get_one_order(int id)
        {
            Order to_show = orders.FirstOrDefault(order => order.Id == id);
            if (to_show is null)
                return null;
            return to_show;
        }
        public int Edit_order(int id, Order new_order)
        {
            Order to_edit = orders.FirstOrDefault(order => order.Id == id);
            if (to_edit is null)
                return 404;
            orders.Remove(to_edit);
            if (Check_id(new_order, orders))
            {
                orders.Add(new_order);
                return 203;
            }
            return 401;
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
                if (prop.Name == sort_by_this && sort_direction == "decs")
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
        private bool Check_id(Order ord, List<Order> lst)
        {
            foreach (var order in lst)
            {
                if(ord.Id == order.Id)
                {
                    return false;
                }
            }
            return true;
        }
    }
}
