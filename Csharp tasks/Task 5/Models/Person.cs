using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace Task_5.Models
{
    public enum Roles
    {
        Admin = 1,
        User = 2
    }
    public class Person
    {
        [Key]
        public string Login { get; set; }
        [Required]
        public string Password { get; set; }

        [Required]
        [EnumDataType(typeof(Roles))]
        public string Role { get; set; }
    }

    
}
