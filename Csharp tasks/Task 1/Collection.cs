using Newtonsoft.Json.Linq;
using Newtonsoft.Json.Schema;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace PracticeTask1
{

    class Collection
    {
        private List<Order> order_collection = new List<Order>();

        public void add_order(Order order)
        {
            order_collection.Add(order);
        }

        public void read_from_file(string filepath)
        {
            if (Validation.file_check(filepath))
            {
                string jsonString = File.ReadAllText(filepath);
                List<Object> collection = JsonSerializer.Deserialize<List<Object>>(jsonString);
                int element_number = 0;
                foreach (Object obj in collection)
                {
                    element_number++;
                    try
                    {
                        Order to_add = JsonSerializer.Deserialize<Order>(obj.ToString());
                        if (to_add.all_check())
                        {
                            order_collection.Add(to_add);
                        }
                        else
                        {
                            Console.WriteLine("Error in data in element № {0}", element_number);
                        }
                    }
                    catch
                    {
                        Console.WriteLine("Error in file (wrong json object structure)");
                    }
                }
            }
        }

        public void new_order_input()
        {
            Order to_add = new Order();
            to_add.console_input();
            order_collection.Add(to_add);
        }

        public void write_to_file(string filepath)
        {
            string json_for_file = JsonSerializer.Serialize<List<Order>>(this.order_collection);
            File.WriteAllText(filepath, json_for_file);
        }

        public void print()
        {
            Console.BackgroundColor = ConsoleColor.White;
            Console.ForegroundColor = ConsoleColor.Black;
            Console.WriteLine("\n#*#*#*#*# C O L L E C T I O N #*#*#*#*#\n");
            Console.BackgroundColor = ConsoleColor.Black;
            Console.ForegroundColor = ConsoleColor.Green;
            foreach (Order order in order_collection)
            {
                order.print();
            }
        }

        public void sort(string param)
        {
            if (order_collection.Count() != 0)
            {
                order_collection = order_collection.OrderBy(c =>
                    c.GetType().GetProperty(param).GetValue(c, null)).ToList();
            }
        }

        public void edit_by_id(int id, string field, string new_data)
        {
            if (order_collection.Count() != 0)
            {
                bool edited = false;
                for (var i = 0; i < order_collection.Count(); ++i)
                {
                    if (order_collection[i].Id == id)
                    {
                        edited = true;
                        Order to_replace = (Order)order_collection[i].Clone();
                        if (Enum.IsDefined(typeof(Order.field_are_ints), field))
                            try
                            {
                                Convert.ToInt32(new_data);
                                to_replace.GetType().GetProperty(field).SetValue(to_replace, Convert.ToInt32(new_data));
                            }
                            catch
                            {
                                Console.WriteLine("{0} must be INTEGER", to_replace.GetType().GetProperty(field).Name);
                            }
                        else
                            to_replace.GetType().GetProperty(field).SetValue(to_replace, new_data);

                        if (to_replace.all_check())
                            order_collection[i] = (Order)to_replace.Clone();
                        else
                            Console.WriteLine("Error in entered data");
                    }
                    if (edited)
                        break;
                }
                if (!edited)
                    Console.WriteLine("No order with such id found.");
            }
        }

        public void delete_by_id(int id)
        {
            if (order_collection.Count() != 0)
            {
                bool deleted = false;
                for (var i = 0; i < order_collection.Count(); ++i)
                {
                    if (order_collection[i].Id == id)
                    {
                        deleted = true;
                        order_collection.RemoveAt(i);
                    }
                }
                if (!deleted)
                    Console.WriteLine("No order with such id found. Nothing was deleted");
            }
        }

        public void search(string data)
        {
            if (order_collection.Count() != 0)
            {
                foreach (Order order in order_collection)
                {
                    if (order.found_for_search(data))
                    {
                        order.print();
                    }
                }
            }
        }

    }
}
