﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Web.Routing;

namespace HackatonProject
{
    public class RouteConfig
    {
        public static void RegisterRoutes(RouteCollection routes)
        {
            routes.IgnoreRoute("{resource}.axd/{*pathInfo}");

            routes.MapRoute(
            name: "MisOrdenes",
            url: "MisOrdenes",
            defaults: new { controller = "Home", action = "MisOrdenes" }
            );

            routes.MapRoute(
            name: "AgregarEquipo",
            url: "AgregarEquipo",
            defaults: new { controller = "Home", action = "AgregarEquipo" }
            );

            routes.MapRoute(
            name: "SignUp",
            url: "SignUp",
            defaults: new { controller = "Home", action = "SignUp" }
        );

            routes.MapRoute(
            name: "Login",
            url: "Login",
            defaults: new { controller = "Home", action = "Login" }
        );


            routes.MapRoute(
                name: "Default",
                url: "{controller}/{action}/{id}",
                defaults: new { controller = "Home", action = "Index", id = UrlParameter.Optional }
            );


        }
    }
}
