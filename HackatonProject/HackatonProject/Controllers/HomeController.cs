using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace HackatonProject.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult AgregarEquipo()
        {
            return View();
        }

        public ActionResult SignUp()
        {
            return View();
        }

        public ActionResult Login()
        {
            return View();
        }

        public ActionResult Index()
        {
            return View();
        }

        public ActionResult About()
        {
            ViewBag.Message = "Your application description page.";

            return View();
        }

        public ActionResult Contact()
        {
            ViewBag.Message = "Your contact page.";

            return View();
        }

        public ActionResult MapaDeBusqueda()
        {
            return View();
        }

        public ActionResult hola()
        {
            string hola = "holas";
            return Json(hola, JsonRequestBehavior.AllowGet);
        }
    }
}