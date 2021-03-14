using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace Task_3__API_.Models
{
    public class SpecialForDateValidationAttribute : ValidationAttribute
    {
        protected override ValidationResult IsValid(object value, ValidationContext validationContext)
        {
            DateTime order_date = (DateTime)value;
            DateTime shipped_date = (DateTime)validationContext.ObjectType.GetProperty("Shipped_date").GetValue(validationContext.ObjectInstance, null);
            if (shipped_date >= order_date)
            {
                return ValidationResult.Success;
            }
            return new ValidationResult("Shipped date can`t be before order date!");
        }
    }
}
