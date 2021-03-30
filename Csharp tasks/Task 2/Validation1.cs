using System;
using System.Globalization;
using System.IO;

namespace Task_2
{
    static class Validation1
    {
        static public bool check_id_or_amount(object id)
        {
            if (check_if_int(id))
            {
                return Convert.ToInt32(id) > 0;
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
                return false;
            }
        }

        static public bool check_discount(int discount)
        {
            return discount < 101 && discount > -1;
        }

        static public bool date_check(string date)
        {
            string[] formats = { "yyyy-MM-dd" };
            DateTime dateValue;
            return DateTime.TryParseExact(date, formats,
                                           new CultureInfo("en-US"),
                                           DateTimeStyles.None,
                                           out dateValue);
        }

        static public bool order_shipped_problem_check(string order_date, string shipped_date)
        {
            string formats = "yyyy-MM-dd";
            CultureInfo provider = CultureInfo.InvariantCulture;
            DateTime _order_date = DateTime.ParseExact(order_date, formats,
                                          provider);
            DateTime _shipped_date = DateTime.ParseExact(shipped_date, formats,
                                           new CultureInfo("en-US"));
            return _order_date <= _shipped_date;
        }

        static public bool status_check(string order_status)
        {
            return Enum.IsDefined(typeof(Order.status_variation), order_status);
        }

        static public bool customer_email_check(string customer_email)
        {
            try
            {
                var addr = new System.Net.Mail.MailAddress(customer_email);
                if (addr.Address == customer_email)
                    return true;
                else
                    return false;
            }
            catch
            {
                Console.WriteLine("Wrong format of customer email");
                return false;
            }


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
    }

}
