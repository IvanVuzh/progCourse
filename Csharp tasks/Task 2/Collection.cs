using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;

namespace Task_2
{
    public class Collection<T>
    {
        private List<T> order_collection = new List<T>();

        public void add_order(T order)     
        {
            if(order != null && validate_T(order, 0))
                order_collection.Add(order);
        }    //rdy

        public void read_from_file(string filepath)
        {
            if (Validation1.file_check(filepath))
            {
                string jsonString = File.ReadAllText(filepath);
                var collection = JsonSerializer.Deserialize<List<Object>>(jsonString);      
                int element_number = 0;
                Console.WriteLine($"{collection.GetType().Name}, {collection.Count()}, {collection.FirstOrDefault().GetType().Name}, {typeof(Object)}");
                foreach (var obj in collection)
                {
                    element_number++;
                    try
                    {
                        //Console.WriteLine($"xyi1{element_number}");
                        T to_add = JsonSerializer.Deserialize<T>(obj.ToString());
                        //Console.WriteLine($"xyi2{element_number}");
                        //Console.WriteLine(to_add);
                        if(validate_T(to_add, element_number))
                        {
                            //Console.WriteLine("added");
                            order_collection.Add(to_add);
                        }
                    }
                    catch(Exception e)
                    {
                        Console.WriteLine(e.Message);
                        //Console.WriteLine("Error in data in element № {0}", element_number);
                        Console.WriteLine("Error in file (wrong json object structure)");
                    }
                }
            }
        }   //err

        public void write_to_file(string filepath)
        {
            string json_for_file = JsonSerializer.Serialize<List<T>>(this.order_collection);
            File.WriteAllText(filepath, json_for_file);
        }   //rdy

        public void print()
        {
            Console.BackgroundColor = ConsoleColor.White;
            Console.ForegroundColor = ConsoleColor.Black;
            Console.WriteLine("\n#*#*#*#*# C O L L E C T I O N #*#*#*#*#\n");
            Console.BackgroundColor = ConsoleColor.Black;
            Console.ForegroundColor = ConsoleColor.Green;
            foreach (T order in order_collection)
            {
                Console.WriteLine(order);
            }
        }   //rdy

        public void sort(string param)
        {
            foreach (var item in typeof(T).GetProperties())
            {
                if (item.Name == param)
                {
                    order_collection = order_collection.OrderBy(c =>
                        c.GetType().GetProperty(param).GetValue(c, null)).ToList();
                    return;
                }
                else
                    Console.WriteLine($"{typeof(T).Name} has no {param} Property");
            }
        }       //rdy

        public void edit_by_id(int id, string field, string new_data)
        {
            if (order_collection.Contains(get_item_by_id(id)))
            {
                try
                {
                    T item = get_item_by_id(id);
                    foreach (var prop in typeof(T).GetProperties())
                    {
                        if (prop.Name == field)
                        {
                            if (Enum.IsDefined(typeof(Order.field_are_ints), field))
                                try
                                {
                                    prop.SetValue(item, Convert.ToInt32(new_data));
                                }
                                catch
                                {
                                    throw new InvalidCastException($"Can`t convert {new_data} to int.");
                                }
                            else
                                prop.SetValue(item, new_data);
                        }
                    }
                    Console.WriteLine("Item succesfully edited!");
                }
                catch
                {
                    Console.WriteLine($"No \"{field}\" in {typeof(T)}.");
                }
            }
            else
                Console.WriteLine("No item with such Id.");
        }       //rdy

        public T get_item_by_id(int id)
        {
            try
            {
                return order_collection.Find(item => Convert.ToInt32(item.GetType().GetProperty("Id").GetValue(item, null)) == id);
            }
            catch
            {
                throw new ArgumentException($"No \"Id\" Property in {typeof(T)} or no element with such ID.");
            }
        }       //new

        public void delete_by_id(int id)
        {
            if (order_collection.Contains(get_item_by_id(id)))
            {
                try
                {
                    T item = get_item_by_id(id);
                    order_collection.Remove(item);
                    Console.WriteLine("Item succesfully deleted!");
                }
                catch
                {
                    Console.WriteLine("Unable to delete item.");
                }
            }
            else
                Console.WriteLine("No item with such Id.");
        }       //rdy

        public void search(string data)
        {
            if (order_collection.Count() != 0)
            {
                bool contain = false;
                bool miss = true;
                foreach (T item in order_collection)
                {
                    foreach (var prop in typeof(T).GetProperties())
                    {
                        if (prop.GetValue(item).ToString().ToLower().Contains(data.ToLower()))
                        {
                            contain = true;
                        }
                    }
                    if (contain)
                    {
                        Console.WriteLine(item);
                        miss = false;
                    }
                    contain = false;
                }
                if (miss)
                {
                    Console.WriteLine("No elements with such data");
                }
            }
        }       //rdy

        public bool validate_T(T to_add, int element_number)
        {
            bool err = false;
            foreach (var prop in to_add.GetType().GetProperties())
            {
                if (prop.GetValue(to_add) == null ||
                    prop.PropertyType.Name == "DateTime" && Convert.ToDateTime(prop.GetValue(to_add)) == new DateTime(1, 1, 1))
                {
                    Console.WriteLine($"element no{element_number} invalid: {prop.PropertyType.Name}");
                    err = true;
                }
            }
            if (err)
            {
                Console.WriteLine("Error in data in element № {0}", element_number);
            }
            return !err;
        }
    }
}
