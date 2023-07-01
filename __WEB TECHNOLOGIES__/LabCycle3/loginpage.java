<%-- 
    Document   : index
    Created on : Jul 1, 2023, 4:28:01 PM
    Author     : y21cs185
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
   "http://www.w3.org/TR/html4/loose.dtd">

<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <h1> Login Form </h1>
 <form method="post" action="./LoginDemo">
	Username: <input type="text" name="username"><br>
	Password: <input type="password" name="pass"><br>
        <input type="submit" name="b1" value="login"><br>
            <input type="reset" name="b2" value="clear"><br>
 </form> 
    </body>
</html>

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package p2;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author y21cs185
 */
public class LoginDemo extends HttpServlet {

   public void doPost(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, IOException {

      // Set response content type
      response.setContentType("text/html");

      // Actual logic goes here.
      PrintWriter out = response.getWriter();
      String name=request.getParameter("username");//will return value
      String pwd=request.getParameter("pass");
	  //out.println("Welcome "+name);
      if(name.equalsIgnoreCase("neeraj")&&pwd.equalsIgnoreCase("neeraj"))
          out.println("succeusfully login"+name);
      else
          out.println("unsucceusfully login"+name);
	  out.close();
   }
}
