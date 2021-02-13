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

        [Obsolete]
        public void read_from_file(string filepath)
        {
            if (Validation.file_check(filepath))
            {
                JsonSchema schema = new JsonSchema();
                schema.Type = JsonSchemaType.Object;
                schema.Properties = new Dictionary<string, JsonSchema>
                {
                    { "Id", new JsonSchema { Type = JsonSchemaType.Integer } },
                    { "Order_status", new JsonSchema { Type = JsonSchemaType.String} },
                    { "Amount", new JsonSchema { Type = JsonSchemaType.Integer } },
                    { "Discount", new JsonSchema { Type = JsonSchemaType.Integer } },
                    { "Order_date", new JsonSchema { Type = JsonSchemaType.String } },
                    { "Shipped_date", new JsonSchema { Type = JsonSchemaType.String } },
                    { "Customer_email", new JsonSchema { Type = JsonSchemaType.String } },
                };
                string json_for_orders = File.ReadAllText(filepath);
                //json_for_orders = json_for_orders.Remove(json_for_orders.Length - 1);
                string json_for_order = json_for_orders.Trim('[',']');
                string[] arr = json_for_order.Split('{');
                arr = arr.Skip(1).ToArray();
                for (var i = 0; i < arr.Count(); i++)
                {
                    arr[i] = "{" + arr[i];
                    if (i != arr.Count()-1)
                    {
                        arr[i] = arr[i].Remove(arr[i].Length - 5);
                    }
                    //Console.WriteLine(arr[i]);
                }
                //Console.WriteLine(arr[0]);
                for (var i = 0; i < arr.Count(); i++)
                {
                    JObject order = JObject.Parse(arr[i]);
                    bool valid = order.IsValid(schema);
                    if (valid)
                    {
                        Order new_order = JsonSerializer.Deserialize<Order>(arr[i]);
                        //new_order.print();
                        //Console.WriteLine(new_order.GetType());
                        if (new_order.all_check())
                            order_collection.Add(new_order);
                        else
                            Console.WriteLine("Error adding new order to list");
                    }
                    else
                        Console.WriteLine("Error in data for element №{0}", i+1);
                }
                //Console.WriteLine(json_for_order);
                //List<string> new_list = JsonSerializer.Deserialize<List<string>>(json_for_orders);
                //List<Order> new_list = JsonSerializer.Deserialize<List<Order>>(json_for_orders);
                //order_collection = new_list;
                //foreach (string s in new_list)
                //{
                //    Console.WriteLine(s);
                //}
                //this.print();
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
            //string res = "";
            //foreach (Order order in this.order_collection)
            //{
            //    res += order.str_for_file() + "\n";
            //}
            //res = res.Remove(res.Length - 1);
            //File.WriteAllText(filepath, res);
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
                //order_collection.Sort( (x, y) =>
                //x.GetType().GetProperty(param).GetValue(x, null).CompareTo ( y.GetType().GetProperty(param).GetValue(y, null)));
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
                        if(field == "Id" || field == "Amount" || field == "Discount")
                            order_collection[i].GetType().GetProperty(field).SetValue(order_collection[i], Convert.ToInt32(new_data));
                        else
                            order_collection[i].GetType().GetProperty(field).SetValue(order_collection[i], new_data);
                        //order_collection[i].print();
                    }
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
                /* не працює бо в цій версії нема перевірки на дублікат ід, і може вилетіли при двох однакових ід
                 var itemToRemove = order_collection.SingleOrDefault(r => r.Id == id);
                 if (itemToRemove != null)
                    order_collection.Remove(itemToRemove);
                 */
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
