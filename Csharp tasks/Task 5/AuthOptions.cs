using Microsoft.IdentityModel.Tokens;
using System.Text;

namespace Task_5
{
    public class AuthOptions
    {
        public const string ISSUER = "HOPETHISWORKS"; 
        public const string AUDIENCE = "HELPMEPLEASE"; 
        const string KEY = "Postavte10Bud'Laska";   
        public const int LIFETIME = 1; 
        public static SymmetricSecurityKey GetSymmetricSecurityKey()
        {
            return new SymmetricSecurityKey(Encoding.ASCII.GetBytes(KEY));
        }
    }
}
