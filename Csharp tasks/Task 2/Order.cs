using System;
using System.Reflection;
using System.Text.Json;

namespace Task_2
{
    class Order : ICloneable
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
                if(Validation1.check_id_or_amount(value))
                    id = value;
                else
                    Console.WriteLine("Id data error");
            }
        }
        public string Order_status
        {
            get => order_status;
            set
            {
                if (Validation1.status_check(value))
                {
                    order_status = value;
                }
                else
                    Console.WriteLine("Order status data error");
            }
        }
        public int Amount
        {
            get => amount;
            set
            {
                if (Validation1.check_id_or_amount(value))
                    amount = value;
                else
                    Console.WriteLine("Amount data error");
            }
        }
        public int Discount
        {
            get => discount;
            set
            {
                if (Validation1.check_discount(value))
                    discount = value;
                else
                    Console.WriteLine("Discount data error");

            }
        }
        public string Order_date
        {
            get => order_date;
            set
            {
                if (Validation1.date_check(value))
                    order_date = value;
                else
                    Console.WriteLine("Order_date data error");

            }
        }
        public string Shipped_date
        {
            get => shipped_date;
            set
            {
                if (Validation1.date_check(value))
                {
                    if(Validation1.order_shipped_problem_check(Order_date, value))
                        shipped_date = value;
                    else
                        Console.WriteLine("Shipped_date is before Order_date error");
                }
                else
                    Console.WriteLine("Shipped_date data error");
            }
        }
        public string Customer_email
        {
            get => customer_email;
            set
            {
                if (Validation1.customer_email_check(value))
                    customer_email = value;
                else
                    Console.WriteLine("Customer_email data error");
            }
        }
        public override string ToString()
        {
            string res = "\n###### O R D E R ######\n";
            foreach (PropertyInfo prop in typeof(Order).GetProperties())
            {
                res += $"{prop.Name} = {prop.GetValue(this)}\n";
            }
            res += "#######################\n";
            return res;
        }
        public string str_for_file()
        {
            string json_for_file = JsonSerializer.Serialize<Order>(this);
            return json_for_file;
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

        public static Order console_input()
        {
            Order res = new Order();
            string input;
            foreach (PropertyInfo prop in res.GetType().GetProperties())
            {
                Console.WriteLine("Enter order {0}", prop.Name);
                input = Console.ReadLine();
                if (Enum.IsDefined(typeof(Order.field_are_ints), prop.Name))
                {
                    try
                    {
                        Convert.ToInt32(input);
                        prop.SetValue(res, Convert.ToInt32(input));
                    }
                    catch
                    {
                        Console.WriteLine("{0} must be INTEGER", prop.Name);
                    }
                }
                else
                {
                    prop.SetValue(res, input);
                }
            }
            return res;
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
