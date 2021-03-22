using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Task_4.Models;

namespace Task_4.Services
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
            return (to_return, to_return.Count);
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
    }
}
