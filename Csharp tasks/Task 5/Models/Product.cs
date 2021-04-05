using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace Task_5.Models
{
    public class Product
    {
        [Key]
        public int Id { get; set; }

        [Required]
        [Range(0, 10000, ErrorMessage ="Amount must be 0-10000")]
        public int Amount { get; set; }
    }
}
