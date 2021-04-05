using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Task_5.Models;
using Task_5.Services;
using Microsoft.IdentityModel.Tokens;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;

namespace Task_5.Controllers
{
    [Produces("application/json")]
    [Route("api/")]
    [ApiController]
    [Authorize]
    public class UserController : ControllerBase
    {

        protected ILogicManager logic_operations;
        public UserController(ILogicManager logic)
        {
            logic_operations = logic;
        }

        [HttpGet]
        [Route("myorders/")]
        public ActionResult Get_my_orders()
        {
            var res = logic_operations.Get_my_orders(User.Identity.Name);
            if (res is null)
                return NotFound();
            return Ok(new { status = 200, message = res });
        }

        [HttpGet]
        [Route("myorders/{id}")]
        public ActionResult Get_my_one_order(int id)
        {
            var res = logic_operations.Get_my_one_order(User.Identity.Name, id);
            if (res is null)
                return NotFound();
            return Ok(new { status = 200, message = res });
        }


        [HttpPost]
        [Route("myorders/")]
        public ActionResult Create_my_order([FromBody] PersonalOrderCreationData orderData)
        {
            var res = logic_operations.Create_my_order(User.Identity.Name, orderData);
            if (res is null)
                return BadRequest(new {status=400, message="Error making order. Check product id and amount ordered" });
            return Ok(new { status = 200, message = res });
        }










        [AllowAnonymous]
        [HttpPost("/login")]
        public IActionResult Token([FromBody] LoginData data)
        {
            var identity = logic_operations.GetIdentity(data.Username, data.Password);
            //return Ok($"{LogicManager.HashPassword(data.Password)}");
            if (identity == null)
            {
                return NotFound();
            }

            var now = DateTime.UtcNow;
            // JWT creation
            JwtSecurityToken jwt = new JwtSecurityToken(
                    issuer: AuthOptions.ISSUER,
                    audience: AuthOptions.AUDIENCE,
                    claims: identity.Claims,
                    expires: now.Add(TimeSpan.FromMinutes(AuthOptions.LIFETIME)),
                    signingCredentials: new SigningCredentials(AuthOptions.GetSymmetricSecurityKey(), SecurityAlgorithms.HmacSha256));
            var encodedJwt = new JwtSecurityTokenHandler().WriteToken(jwt);

            var response = new
            {
                access_token = encodedJwt,
                username = identity.Name
            };

            return Ok(new { status = "200", message = response });
        }

        [AllowAnonymous]
        [HttpPost("/register")]
        public IActionResult RegisterUser([FromBody] LoginData data)
        {
            var res = logic_operations.AddUser(data.Username, data.Password);
            if (res == null)
                return BadRequest(new { status = "401", message="Error creating profile."});
            return Ok(new { status = "200", message = res });
        }

        
    }
}
