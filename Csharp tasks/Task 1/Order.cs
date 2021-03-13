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
    class Order: ICloneable
    {
        protected int id;
        protected string order_status;
        protected int amount;
        protected int discount;
        protected string order_date;
        protected string shipped_date;
        protected string customer_email;


        public enum status_variation //useless 
        {
            paid = 1,
            not_paid = 2,
            refunded = 3
        }
        public enum field_are_ints //useless 
        {
            Id = 1,
            Amount = 2,
            Discount = 3
        }
        public int Id
        {
            get => id;
            set
            {
                id = Validation.check_id_or_amount(value) ? value : -1;
            }
        }
        public string Order_status
        {
            get => order_status;
            set
            {
                if (!Validation.status_check(value))
                {
                    Console.WriteLine("Order status data error");
                    id = -1;
                }
                order_status = value;
            }
        }
        public int Amount
        {
            get => amount;
            set
            {
                if (!Validation.check_id_or_amount(value))
                    id = -1;
                amount = value;
            }
        }
        public int Discount
        {
            get => discount;
            set
            {
                if (!Validation.check_discount(value))
                    id = -1;
                discount = value;
            }
        }
        public string Order_date
        {
            get => order_date;
            set
            {
                if (!Validation.date_check(value))
                    id = -1;
                order_date = value;

            }
        }
        public string Shipped_date
        {
            get => shipped_date;
            set
            {
                if (!Validation.date_check(value))
                    id = -1;
                shipped_date = value;
            }
        }
        public string Customer_email
        {
            get => customer_email;
            set
            {
                if (!Validation.customer_email_check(value))
                    id = -1;
                customer_email = value;
            }
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
            foreach (PropertyInfo prop in this.GetType().GetProperties())
            {
                if (prop.GetValue(this) is null)
                    return false;
            }
            if (id == -1)
                return false;
            else
            {
                if (!Validation.order_shipped_problem_check(this.order_date, this.shipped_date))
                {
                    Console.WriteLine("Date of order must be made before shipping goods");
                    return false;
                }
            }
            return true;
        }

        public bool found_for_search(string data)
        {
            bool res = false;
            PropertyInfo[] properties = typeof(Order).GetProperties();
            foreach (PropertyInfo property in properties)
            {
                if (Convert.ToString(property.GetValue(this)).Contains(data))
                {
                    res = true;
                }
            }
            return res;
        }

        public void console_input()
        {

            string input;
            foreach (PropertyInfo prop in this.GetType().GetProperties())
            {
                Console.WriteLine("Enter order {0}", prop.Name);
                input = Console.ReadLine();
                if (Enum.IsDefined(typeof(Order.field_are_ints), prop.Name))
                {
                    try
                    {
                        Convert.ToInt32(input);
                        prop.SetValue(this, Convert.ToInt32(input));
                    }
                    catch
                    {
                        Console.WriteLine("{0} must be INTEGER", prop.Name);
                    }
                }
                else
                {
                    prop.SetValue(this, input);
                }
            }
        }

        public object Clone()
        {
            Order o = new Order();
            foreach (PropertyInfo prop in this.GetType().GetProperties())
            {
                prop.SetValue(o, prop.GetValue(this));
            }
            return o;
        }
    }
}
