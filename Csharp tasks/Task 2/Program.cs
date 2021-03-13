using System;
using System.Collections.Generic;

namespace Task_2
{
    class Test
    {
        public int Int { get; set; }
        public int Id { get; set; }
        public override string ToString()
        {
            return $"Int: {Int}\n Id: {Id}";
        }
    }
    class Program
    {
        [Obsolete]
        static void Main(string[] args)
        {
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("Enter path to data file:");
            string file_path = Console.ReadLine();
            //          "E:/Практика С#/Task 2/data.json"
            //          "E:/Практика С#/PracticeTask1/PracticeTask1/Baddata.json"

            Collection<Order> collection = new Collection<Order>();
            collection.read_from_file(file_path);
            collection.print();
            bool do_continue = true;
            while (do_continue)
            {
                int user_choise = menu();
                switch (user_choise)
                {
                    case 1:
                        //search
                        console_color_1();
                        Console.WriteLine("Enter data to be searched:");
                        string to_search = Console.ReadLine();
                        console_color_2();
                        collection.search(to_search);
                        break;
                    case 2:
                        //sort
                        string sorting_param = param_name_input();
                        collection.sort(sorting_param);
                        collection.print();
                        collection.write_to_file(file_path);
                        break;
                    case 3:
                        //delete by id
                        int id_to_delete = id_input();
                        collection.delete_by_id(id_to_delete);
                        collection.print();
                        collection.write_to_file(file_path);
                        break;
                    case 4:
                        //add new order (console)
                        collection.add_order(Order.console_input());
                        collection.print();
                        collection.write_to_file(file_path);
                        break;
                    case 5:
                        //edit order
                        int to_change_id = id_input();
                        string param_name = param_name_input();
                        console_color_1();
                        Console.WriteLine("Enter new value of the chosen data:");
                        string new_value = Console.ReadLine();
                        console_color_2();
                        collection.edit_by_id(to_change_id, param_name, new_value);
                        collection.write_to_file(file_path);
                        collection.print();
                        break;
                    case 6:
                        //exit
                        Console.WriteLine("Have a nice day. Goodbye!");
                        do_continue = false;
                        break;
                }
            }
            Console.ReadKey();
        }

        static int menu()
        {
            int res;
            console_color_1();
            Console.WriteLine("YOU ARE NOW IN MAIN MENU");
            Console.WriteLine("ENTER YOIR CHOICE:");
            console_color_2();
            Console.WriteLine("1 - search some data through all info\n" +
              "2 - sort collection by some argument\n" +
              "3 - delete any order(by its id) and rewrite collection in file\n" +
              "4 - add an order and rewrite collection in file\n" +
              "5 - edit an order and rewrite collection in file\n" +
              "6 - exit program\n");
            string choice = Console.ReadLine();
            while (!Validation1.check_if_int(choice) || Convert.ToInt32(choice) < 1 || Convert.ToInt32(choice) > 6)
            {
                Console.WriteLine("REENTER YOIR CHOICE:");
                choice = Console.ReadLine();
            }
            res = Convert.ToInt32(choice);
            return res;
        }
        static string param_name_input()
        {
            string res;
            console_color_1();
            Console.WriteLine("Enter data to be sorted/edited by: ");
            res = Console.ReadLine();
            console_color_2();
            return res;
        }
        static int id_input()
        {
            int res;
            console_color_1();
            Console.WriteLine("Enter id of order:");
            string input = Console.ReadLine();
            while (!Validation1.check_if_int(input) || Convert.ToInt32(input) < 1)
            {
                Console.WriteLine("Reenter id of order. It must be a natural number.");
                input = Console.ReadLine();
            }
            console_color_2();
            res = Convert.ToInt32(input);
            return res;
        }
        static void console_color_1()
        {
            Console.BackgroundColor = ConsoleColor.White;
            Console.ForegroundColor = ConsoleColor.Black;
        }
        static void console_color_2()
        {
            Console.BackgroundColor = ConsoleColor.Black;
            Console.ForegroundColor = ConsoleColor.Green;
        }
        static Dictionary<string, string> order_fields = new Dictionary<string, string>
            {
                {"1", "Id"},
                {"2", "Order_status"},
                {"3", "Amount"},
                {"4", "Discount" },
                {"5", "Order_date"},
                {"6", "Shipped_date"},
                {"7", "Customer_email"}
            };
    }
}
