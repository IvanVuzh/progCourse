using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Task_4.Services
{
    public interface ILogicManager 
    {
        public (List<Order> res, int count) Index(string s, string sort_by, string sort_order, int offset, int limit);
        public int Create_new_order(Order to_add);
        public (int status, Order res) Delete_order(int id);
        public Order Get_one_order(int id);
        public int Edit_order(int id, Order new_order);
    }
}
