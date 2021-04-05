using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Claims;
using System.Threading.Tasks;
using Task_5.Models;

namespace Task_5.Services
{
    public interface ILogicManager 
    {
        public (List<Order> res, int count) Index(string s, string sort_by, string sort_order, int offset, int limit);
        public int Create_new_order(Order to_add);
        public (int status, Order res) Delete_order(int id);
        public Order Get_one_order(int id);
        public int Edit_order(int id, Order new_order);
        public List<Order> Get_my_orders(string username);
        public Order Get_my_one_order(string username, int id);
        public Order Create_my_order(string username, PersonalOrderCreationData data);
        public Product ChangeProductAmount(int productId, int new_amount);
        public int GetProductAmount(int productId);
        public ClaimsIdentity GetIdentity(string username, string password);
        public Person AddUser(string username, string password);
        public Product AddProduct(int id, int amount);
        public Product DeleteProduct(int id);
    }
}
