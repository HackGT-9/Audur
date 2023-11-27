package preetham.project.first;
import java.io.*;
//import java.nio.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;

//import java.util.*;
import org.springframework.stereotype.Controller;
import org.springframework.ui.*;
import org.springframework.web.bind.annotation.*;
//import javax.servlet.*;
//import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;

import jakarta.servlet.http.HttpServletRequest;

// This is my first Spring Boot app ever, so glad to have pulled it off!
@Controller
public class HiController {

    @GetMapping("/")
    public String home(){
        // System.out.println("BRO I AM HERE");
        return "index";
    }

    @GetMapping("/index.html")
    public String home_again(){
        // System.out.println("BRO I AM HERE");
        return "index";
    }

	@GetMapping("/upload.html")
	public String upload() {
		//model.addAttribute("name", name);
		return "upload";
	}

    @GetMapping("about.html")
    public String about(){
        return "about";
    }

    @PostMapping("song.html")
    public String ret(@RequestParam("file") MultipartFile f, HttpServletRequest request, Model model){
        String title = request.getParameter("titleArea");
        String description = request.getParameter("descriptionArea");
        //MultipartFile file = request.getParameter("file");
        String upload_dir = "C:\\Users\\sthelluri1\\Desktop\\first\\src\\main\\resources\\static";
        // System.out.println(title);
        // System.out.println(description);
        String f_name = f.getOriginalFilename();
        String absolutePath = "";
        //String[] arr = f_name.split("[.]");
        //f_name = arr[0];
        try {
            Path uploadPath = Path.of(upload_dir);
            System.out.println("I GOT THE UPLOAD PATH");
            Path filePath = uploadPath.resolve(f_name);
            // System.out.println(filePath.toString());
            Files.copy(f.getInputStream(), filePath, StandardCopyOption.REPLACE_EXISTING);
            absolutePath = filePath.toAbsolutePath().toString();
            // System.out.println("File saved to: " + absolutePath);

            //redirectAttributes.addFlashAttribute("message", "File uploaded successfully: " + file.getOriginalFilename());
        } catch (IOException e) {
            e.printStackTrace();
            //redirectAttributes.addFlashAttribute("message", "Failed to upload file");
        }
        absolutePath = absolutePath.replace("\\", "/");
        model.addAttribute("title", title);
        model.addAttribute("desc", description);
        model.addAttribute("pth", "/audio/"+f_name);
        model.addAttribute("link", "/audio/"+f_name);
        return "song";
    }

}