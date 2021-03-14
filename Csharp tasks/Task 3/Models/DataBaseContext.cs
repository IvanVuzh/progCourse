using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Task_3__API_.Models
{
    public class DataBaseContext : DbContext
    {
        public DataBaseContext()
        {

        }
        public DataBaseContext(DbContextOptions<DataBaseContext> options) : base(options)
        {

        }
        public DbSet<Order> Orders { get; set; }        
    }
}
