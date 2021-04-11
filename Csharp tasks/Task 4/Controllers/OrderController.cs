using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Task_4.Models;
using Task_4.Services;

namespace Task_4.Controllers
{
    [Produces("application/json")]
    [Route("api/")]
    [ApiController]
    public class OrdersController : ControllerBase
    {
        private ILogicManager logic_operations;
        public OrdersController(ILogicManager logic)
        {
            logic_operations = logic;
        }
        Dictionary<int, string> status_list = new Dictionary<int, string>
        {
            {201, "Order was succesfuly created"},
            {202, "Order was succesfuly deleted"},
            {203, "Order was succesfuly edited"},
            {401, "Order with such Id already exists"}
        };

        /// <summary>
        /// Fetches all events / Finds specific Events using partial match / Sorts / Uses pagination
        /// </summary>
        /// <param name="s" example="paid">Filters events with partial search   </param> 
        /// <param name="sort_by" example="Id">Sorting parameter   </param> 
        /// <param name="sort_order" example="desc"> Ascending/Descending sorting   </param> 
        /// <param name="offset" example="0">Page number   </param> 
        /// <param name="limit" example="0">Contains a page with limited amout of events   </param> 
        /// <returns>A List with searched Orders and amount of Orders in it</returns>
        [HttpGet]
        [Route("get/")]
        public ActionResult Index(string s, string sort_by, string sort_order, int offset, int limit)
        {
            var res = logic_operations.Index(s, sort_by, sort_order, offset, limit);
            if(res.count == 0)
            {
                return BadRequest("No orders with such data");
            }
            return Ok(new {res.res, res.count});
        }


        /// <summary>
        /// Adds given Order to DataBase
        /// </summary>
        /// <remarks>
        /// Sample request:
        ///
        ///     Post 
        ///     {
        ///        "id": 1,
        ///        "order_status": "paid",
        ///        "amount": 1,
        ///        "discount": 1,
        ///        "order_date": "2010-10-10T00:00:00",
        ///        "shipped_date": "2010-10-10T00:00:00",
        ///        "customer_email": "emailexample@gmail.com"
        ///     }
        ///
        /// </remarks>
        /// <returns> 201 response code and success message </returns>
        [HttpPost]
        [Route("orders/")]                                       
        public ActionResult Create_new_order(Order to_add)
        {
            if (ModelState.IsValid)
            {
                int res = logic_operations.Create_new_order(to_add);
                string message = $"status: {res} " +
                        $"message: {status_list[res]}";
                if (res == 201)
                {
                    return Ok(message);
                }
                return BadRequest(message);
            }
            return BadRequest("Bad Order data.");
        }

        /// <summary>
        /// Deletes Order with given Id from DataBase
        /// </summary>
        /// <param name="id" example="1">Id of event to find</param>
        /// <returns> 202 response code and success message</returns>
        [HttpDelete]
        [Route("orders/{id}")]                             
        public ActionResult Delete_order(int id)
        {
            var res = logic_operations.Delete_order(id);
            if (res.res == null)
            {
                return NotFound();
            }
            return Ok($"status: {res.status} " +
                $"message: {status_list[res.status]}");
        }

        /// <summary>
        /// Edits existing order by its id with data of given Order
        /// </summary>
        /// <param name="id" example="1">Id of order to edit</param>
        /// <param name="new_order">New Order data</param> 
        /// <remarks>
        /// Sample request:
        ///
        ///     Put /1
        ///     {
        ///        "id": 1,
        ///        "order_status": "paid",
        ///        "amount": 1,
        ///        "discount": 1,
        ///        "order_date": "2010-10-10T00:00:00",
        ///        "shipped_date": "2010-10-10T00:00:00",
        ///        "customer_email": "emailexample@gmail.com"
        ///     }
        ///
        /// </remarks>
        /// <returns> 203 response code and success message </returns>
        [HttpPut]
        [Route("orders/{id}")]
        public ActionResult Edit_order(int id, Order new_order)
        {
            if (ModelState.IsValid)
            {
                int res = logic_operations.Edit_order(id, new_order);
                switch (res)
                {
                    case 404: return NotFound();
                    case 203:
                        return Ok($"status: {res} " +
                      $"message: {status_list[res]}");
                    case 401:
                        return BadRequest($"status: {res} " +
                $"message: {status_list[res]}");
                }
            }
            return BadRequest($"status: 402 " +
                  $"message: Bad Order data.");
        }
        /// <summary>
        /// Finds a specific Event by given id
        /// </summary>
        /// <param name="id" example="1">Id of event to find</param> 
        /// <returns> 200 response code and found Order </returns>
        [HttpGet]
        [Route("orders/{id}")]
        public ActionResult Get_one_order(int id)
        {
            if (logic_operations.Get_one_order(id) is null)
                return NotFound();
            return Ok(logic_operations.Get_one_order(id));
        }


    }
}
