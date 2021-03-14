using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Task_3__API_.Models;

namespace Task_3__API_.Controllers
{
    [Route("api/")]
    [ApiController]
    public class OrdersController : ControllerBase
    {
        private DataBaseContext DBContext = new DataBaseContext();
        public OrdersController(DataBaseContext ctx)
        {
            DBContext = ctx;
        }

        [HttpGet]
        [Route("get/")]
        public ActionResult Index(string s, string sort_by_this, string sort_direction, int page_num, int page_size)
        {
            //ненавиджу пагінацію
            List<Order> list_of_orders = new List<Order>();
            if (s != null)
                list_of_orders = Search(DBContext.Orders.ToList(), s);
            else
                list_of_orders = DBContext.Orders.ToList();
            //TODO sort
            list_of_orders = Sort(list_of_orders, sort_direction, sort_by_this);

            if (page_size == null || page_size < 1)
            {
                page_size = list_of_orders.Count;
            }
            if (page_num == null || page_num < 1)
                page_num = 1;
            List<Order> to_return = Paginate(list_of_orders, page_num, page_size);
            return Ok(to_return);
        }

        [HttpPost]
        [Route("orders/")]
        public ActionResult Create_new_order(Order to_add)
        {
            //return Ok(list_of_ids);
            if (ModelState.IsValid)
            {
                try
                {
                    DBContext.Orders.Add(to_add);
                    DBContext.SaveChanges();
                    return Ok($"{to_add.Id} was added");
                }
                catch
                {
                    return BadRequest("Order with with id already exist");
                }
            }
            return BadRequest("Invalid data");
        }


        [HttpDelete]
        [Route("orders/{id}")]
        public ActionResult Delete_order(int id)
        {
            Order to_remove = DBContext.Orders.FirstOrDefault(order => order.Id == id);
            if (to_remove is null)
                return NotFound();
            DBContext.Orders.Remove(to_remove);
            DBContext.SaveChanges();
            return Ok($"{id} was deleted");
        }

        [HttpPut]
        [Route("orders/{id}")]
        public ActionResult Edit_order(int id, Order new_order)
        {
            Order to_edit = DBContext.Orders.FirstOrDefault(order => order.Id == id);
            if (to_edit is null)
                return NotFound();
            foreach (var prop in to_edit.GetType().GetProperties())
            {
                prop.SetValue(to_edit, new_order.GetType().GetProperty(prop.Name).GetValue(new_order));
            }
            DBContext.Orders.Update(to_edit);
            DBContext.SaveChanges();
            return Ok($"{id} was edited");
        }

        [HttpGet]
        [Route("orders/{id}")]
        public ActionResult Get_one_order(int id)
        {
            Order to_show = DBContext.Orders.FirstOrDefault(order => order.Id == id);
            if (to_show is null)
                return NotFound();
            return Ok(to_show);
        }

        public List<Order> Search(List<Order> coll, string search_data)
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
        public List<Order> Paginate(List<Order> coll, int page_num, int page_size)
        {
            List<Order> res = coll.Skip((page_num - 1) * page_size).Take(page_size).ToList();
            return res;
        }
        public List<Order> Sort(List<Order> coll, string sort_direction, string sort_by_this)
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
        public enum Sort_directions
        {
            asc = 1,
            desc = 2
        }
    }
}
