using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PracticeTask1
{
    static class Validation
    {
        static public bool check_id_or_amount(object id)
        {
            if (check_if_int(id))
            {
                //Console.WriteLine("Id is int");
                if (Convert.ToInt32(id) < 1)
                {
                    //throw new ArithmeticException("Error, id is not natural number");
                    //Console.WriteLine("Id or amount must be a natural number");
                    return false;
                }
                else
                {
                    //Console.WriteLine("ELSE");
                    return true;
                }
            }
            else
                return false;
        }

        static public bool check_if_int(object data)
        {
            try
            {
                Convert.ToInt32(data);
                return true;
            }
            catch
            {
                //Console.WriteLine("Data is not integer");
                return false;
            }
        }

        static public bool check_discount(int discount)
        {
            if (discount > 100 && discount < 0)
            {
                //Console.WriteLine("Discount must be in range 0-100");
                return false;
            }
            else
                return true;
        }

        static public bool file_check(string filename)
        {
            if (!File.Exists(filename))
            {
                Console.WriteLine("Error reading file. File does not exist or invalid filepath entered");
                return false;
            }
            var info = new FileInfo(filename);
            if (info.Length == 0)
                return false;
            else if (info.Length < 6)
            {
                var content = File.ReadAllText(filename);
                Console.WriteLine("Error reading file. File is empty");
                return content.Length == 0;
            }
            else
                return true;
        }

        static public bool date_check(string date)
        {
            string[] formats = {"yyyy-MM-dd"};
            DateTime dateValue;
            if (DateTime.TryParseExact(date, formats,
                                           new CultureInfo("en-US"),
                                           DateTimeStyles.None,
                                           out dateValue))
            {
                //Console.WriteLine("Converted '{0}' to {1}.", date, dateValue);
                return true;
            }
            else
            {
                //Console.WriteLine("Unable to convert '{0}' to a date.", date);
                return false;
            }
        }

        static public bool order_shipped_problem_check(string order_date, string shipped_date)
        {
            string formats = "yyyy-MM-dd";
            CultureInfo provider = CultureInfo.InvariantCulture;
            DateTime _order_date = DateTime.ParseExact(order_date, formats,
                                          provider);
            DateTime _shipped_date = DateTime.ParseExact(shipped_date, formats,
                                           new CultureInfo("en-US"));
            if (_order_date > _shipped_date)
            {
                //Console.WriteLine("Date of order must be made before shipping goods");
                return false;
            }
            else
                return true;
        }

        static public bool status_check(string order_status)
        {
            if (order_status == "paid" || order_status == "not paid" || order_status == "refunded")
                return true;
            else
            {
                //Console.WriteLine("Invalid order status entered");
                return false;
            }
        }

        static public bool customer_email_check(string customer_email)
        {
            try
            {
                var addr = new System.Net.Mail.MailAddress(customer_email);
                if (addr.Address == customer_email)
                    return true;
                else
                {
                    //Console.WriteLine("Invalid customer email adress");
                    return false;
                }
            }
            catch
            {
                //Console.WriteLine("Invalid customer email adress");
                return false;
            }
        }
    }
}
