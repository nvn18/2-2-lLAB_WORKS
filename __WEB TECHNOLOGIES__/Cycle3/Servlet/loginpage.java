

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
public class loginpage extends HttpServlet {

   public void doPost(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, IOException {

      // Set response content type
      response.setContentType("text/html");

      // Actual logic goes here.
      PrintWriter out = response.getWriter();
      String name=request.getParameter("username");//will return value
      String pwd=request.getParameter("pass");
	  //out.println("Welcome "+name);
      if(name.equalsIgnoreCase("NVN")&&pwd.equalsIgnoreCase("AURORA"))
          out.println("succeusfully login"+name);
      else
          out.println("unsucceusfully login"+name);
	  out.close();
   }
}
