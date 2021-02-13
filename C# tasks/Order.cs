using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;
using System.Text.Json;
using Newtonsoft.Json.Schema;
using Newtonsoft.Json.Linq;

namespace PracticeTask1
{
    class Order
    {
        protected int id;
        protected string order_status;
        protected int amount;
        protected int discount;
        protected string order_date;
        protected string shipped_date;
        protected string customer_email;

        public int Id
        {
            get => id;
            set 
            {
                if (Validation.check_id_or_amount(value))
                    id = value;
                else
                    id = -1;
            }
        }
        public string Order_status
        {
            get => order_status;
            set
            {
                if (Validation.status_check(value))
                    order_status = value;
                else
                    order_status = "invalid";
            }
        }
        public int Amount
        {
            get => amount;
            set
            {
                if (Validation.check_id_or_amount(value))
                    amount = value;
                else
                    amount = -1;
            }
        }
        public int Discount
        {
            get => discount;
            set
            {
                if (Validation.check_discount(value))
                    discount = value;
                else
                    discount = -1;
            }
        }
        public string Order_date
        {
            get => order_date;
            set
            {
                if (Validation.date_check(value))
                    order_date = value;
                else
                    order_date = "invalid";
            }
        }
        public string Shipped_date
        {
            get => shipped_date;
            set
            {
                if (Validation.date_check(value))
                    shipped_date = value;
                else
                    shipped_date = "invalid";
            }
        }
        public string Customer_email
        {
            get => customer_email;
            set
            {
                if (Validation.customer_email_check(value))
                    customer_email = value;
                else
                    customer_email = "invalid";
            }
        }

        public Order(int _id, string _order_status, int _amount, int _discount, string _order_date, string _shipped_date, string _customer_email)
        {
            Id = _id;
            Order_status = _order_status;
            Amount = _amount;
            Discount = _discount;
            Order_date = _order_date;
            Shipped_date = _shipped_date;
            Customer_email = _customer_email;
        }

        public Order()
        {
            Id = -1;
            Order_status = "invalid";
            Amount = -1;
            Discount = -1;
            Order_date = "invalid";
            Shipped_date = "invalid";
            Customer_email = "invalid";
        }

        public void print()
        {
            Console.WriteLine("\n###### O R D E R ######");
            foreach (PropertyInfo prop in typeof(Order).GetProperties())
            {
                Console.WriteLine("{0} = {1}", prop.Name, prop.GetValue(this));
            }
            Console.WriteLine("#######################\n");
        }

        public string str_for_file()
        {
            string json_for_file = JsonSerializer.Serialize<Order>(this);
            return json_for_file;
        }      
        public bool all_check()
        {
            bool res = true;
            bool date_prob = false;
            if (this.id == -1)
            {
                Console.WriteLine("Invalid id");
                res = false;
            }
            if (this.order_status == "invalid")
            {
                Console.WriteLine("Invalid order status");
                res = false;
            }
            if (this.amount == -1)
            {
                Console.WriteLine("Invalid amount");
                res = false;
            }
            if (this.discount == -1)
            {
                Console.WriteLine("Invalid discount");
                res = false;
            }
            if (this.order_date == "invalid")
            {
                Console.WriteLine("Invalid order date");
                res = false;
                date_prob = true;
            }
            if (this.shipped_date == "invalid")
            {
                Console.WriteLine("Invalid shipped date");
                res = false;
                date_prob = true;
            }
            if (this.customer_email == "invalid")
            {
                Console.WriteLine("Invalid customer email");
                res = false;
            }
            if (!date_prob)
            {
                if (!Validation.order_shipped_problem_check(this.order_date, this.shipped_date))
                {
                    Console.WriteLine("Date of order must be made before shipping goods");
                    res = false;
                }
            }
            return res;
        }

        public bool found_for_search(string data)
        {
            bool res = false;
            PropertyInfo[] properties = typeof(Order).GetProperties();
            foreach (PropertyInfo property in properties)
            {
                if(Convert.ToString(property.GetValue(this)).Contains(data))
                {
                    //Console.WriteLine("Found");
                    res = true;
                }
            }
            return res;
        }

        public void console_input()
        {
            string input;


            Console.WriteLine("Enter id:");
            input = Console.ReadLine();
            while (!Validation.check_if_int(input) || Convert.ToInt32(input) < 1)
            {
                Console.WriteLine("Reenter id:");
                input = Console.ReadLine();
            }
            this.Id = Convert.ToInt32(input);


            Console.WriteLine("Enter order status:");
            input = Console.ReadLine();
            while (!Validation.status_check(input))
            {
                Console.WriteLine("Reenter order status:");
                input = Console.ReadLine();
            }
            this.Order_status = input;


            Console.WriteLine("Enter amount:");
            input = Console.ReadLine();
            while (!Validation.check_if_int(input) || Convert.ToInt32(input) < 1)
            {
                Console.WriteLine("Reenter amount:");
                input = Console.ReadLine();
            }
            this.Amount = Convert.ToInt32(input);


            Console.WriteLine("Enter discount:");
            input = Console.ReadLine();
            while (!Validation.check_if_int(input) || Convert.ToInt32(input) < 0 || Convert.ToInt32(input) > 100)
            {
                Console.WriteLine("Reenter discount:");
                input = Console.ReadLine();
            }
            this.Discount = Convert.ToInt32(input);


            bool date_problem = true;
            while (date_problem)
            { 
                Console.WriteLine("Enter order date:");
                input = Console.ReadLine();
                while (!Validation.date_check(input))
                {
                    Console.WriteLine("Reenter order date:");
                    input = Console.ReadLine();
                }
                this.Order_date = input;


                Console.WriteLine("Enter shipped date:");
                input = Console.ReadLine();
                while (!Validation.date_check(input))
                {
                    Console.WriteLine("Reenter shipped date:");
                    input = Console.ReadLine();
                }
                this.Shipped_date = input;

                if (Validation.order_shipped_problem_check(this.Order_date, this.Shipped_date))
                {
                    date_problem = false;
                }
                else
                    Console.WriteLine("Date of order must be made before shipping goods");
            }

            Console.WriteLine("Enter customer email:");
            input = Console.ReadLine();
            while (!Validation.customer_email_check(input))
            {
                Console.WriteLine("Reenter customer email:");
                input = Console.ReadLine();
            }
            this.Customer_email = input;

            
        }
    }
}
