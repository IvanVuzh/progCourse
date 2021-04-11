using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;
using Task_4.Models;

namespace Task_4
{
    public class Order
    {
        [Key]
        public int Id { get; set; }

        [Required]
        public string Order_status { get; set; }

        [Required]
        [Range(1, 1000, ErrorMessage = "Amount must be a natural integer (1-1000)")]
        public int Amount { get; set; }

        [Required]
        [Range(0, 100, ErrorMessage = "Discount must be a natural integer (0-100)")]
        public int Discount { get; set; }

        [Required]
        [SpecialForDateValidation]
        public DateTime Order_date { get; set; }

        [Required]
        public DateTime Shipped_date { get; set; }

        [Required]
        [DataType(DataType.EmailAddress)]
        public string Customer_email { get; set; }
    }
}
