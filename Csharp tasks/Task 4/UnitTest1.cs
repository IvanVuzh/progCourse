using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using Task_4.Controllers;
using Task_4.Services;
using Xunit;

namespace Task_4.Tests
{
    public class UnitTest1
    {
        OrdersController controller;
        ILogicManager service;

        public UnitTest1()
        {
            service = new TestOrderService();
            controller = new OrdersController(service);
        }
        [Fact]
        public void Index_ReturnsOK()
        {
            Assert.IsType<OkObjectResult>(controller.Index("", "", "", 0, 0));
        }
        [Fact]
        public void CreateNewOrder_InvalidObjectPassed_ReturnsBadRequest()
        {
            // Arrange
            Order idMissingItem = new Order()
            {
                Order_status = "paid",
                Amount = 100,
                Discount = 0,
                Order_date = new DateTime(2010, 2, 2),
                Shipped_date = new DateTime(2011, 2, 2),
                Customer_email = "email6@gmail.com"
            };
            controller.ModelState.AddModelError("Id", "Required");
            // Act
            var badResponse = controller.Create_new_order(idMissingItem);
            // Assert
            Assert.IsType<BadRequestObjectResult>(badResponse);
        }

        [Fact]
        public void Paginate_ReturnsOK()
        {
            Assert.IsType<OkObjectResult>(controller.Index("", "", "", 3, 1));      ///верне третій елемент
        }
        [Fact]
        public void GetOne_ReturnsRight()
        {
            var check = new Order
            {
                Id = 6,
                Order_status = "paid",
                Amount = 100,
                Discount = 0,
                Order_date = new DateTime(2010, 2, 2),
                Shipped_date = new DateTime(2011, 2, 2),
                Customer_email = "email6@gmail.com"
            };
            var result = controller.Get_one_order(6) as OkObjectResult;
            var order = Assert.IsType<Order>(result.Value);
            Assert.Equal(order.Customer_email, check.Customer_email);
        }
        [Fact]
        public void GetOneOrder_InvalidId_ReturnsBadRequest()
        {
            Assert.IsType<NotFoundResult>(controller.Get_one_order(10));
        }
        [Fact]
        public void DeleteOrder_ReturnsOK()
        {
            Order ord = new Order
            {
                Id = 1,
                Order_status = "not paid",
                Amount = 10,
                Discount = 50,
                Order_date = new DateTime(2020, 5, 6),
                Shipped_date = new DateTime(2020, 5, 13),
                Customer_email = "email1@gmail.com"
            };
            Assert.IsType<OkObjectResult>(controller.Edit_order(1, ord));
        }
        [Fact]
        public void BadIdDeleteOrder_ReturnsBadRequest()
        {
            Order ord = new Order
            {
                Id = 1,
                Order_status = "not paid",
                Amount = 10,
                Discount = 50,
                Order_date = new DateTime(2020, 5, 6),
                Shipped_date = new DateTime(2020, 5, 13),
                Customer_email = "email1@gmail.com"
            };
            Assert.IsType<NotFoundResult>(controller.Edit_order(10, ord));
        }
        [Fact]
        public void DeleteOrder_BadNewOrder_ReturnsBadRequest()
        {
            Order ord = new Order
            {
                Order_status = "not paid",
                Amount = 10,
                Discount = 50,
                Order_date = new DateTime(2020, 5, 6),
                Shipped_date = new DateTime(2020, 5, 13),
                Customer_email = "email1@gmail.com"
            };
            controller.ModelState.AddModelError("Id", "Required");
            Assert.IsType<BadRequestObjectResult>(controller.Edit_order(1, ord));
        }
        [Fact]
        public void Index_SortIdDecs_RetursOk()
        {
            Assert.IsType<OkObjectResult>(controller.Index("", "Id", "decs", 0, 0));
        }
        [Fact]
        public void SortId_WorksRight()
        {
            var req = service.Index("", "Id", "decs", 0, 0);
            Assert.Equal(6, req.res[0].Id);
        }
        [Fact]
        public void Paginate_ReturnsWrightAmount()
        {
            var req = service.Index("", "", "", 2, 5);
            Assert.Equal(1, req.count);
        }
        [Fact]
        public void Search_ReturnsWrightAmount()
        {
            var req = service.Index("paid", "", "", 0, 0);
            Assert.Equal(5, req.count);
        }
    }
}
