using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace Task_5.Models
{

    public class LoginData
    {
        public string Username { get; set; }
        public string Password { get; set; }
    }

    public class PersonalOrderCreationData
    {
        [Required]
        public DateTime Shipped_date { get; set; }

        [Required]
        [Range(1, 1000, ErrorMessage = "Enter valid amount for order (1-1000)")]
        public int Amount { get; set; }

        [Required]
        public int ProductId { get; set; }

    }

    public class ProductData
    {
        [Required]
        public int ProductId { get; set; }

        [Required]
        public int NewAmount { get; set; }

        [Required]
        public string ProductName { get; set; }

    }
}
