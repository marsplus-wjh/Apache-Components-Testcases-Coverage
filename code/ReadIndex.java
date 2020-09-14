
import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;


public class ReadIndex {
    private File url ;
    private static HSSFWorkbook wb = new HSSFWorkbook();
    static HSSFSheet sheet = wb.createSheet("sheet0");
    private static int r = 0;
    private static int c = 0;
 
    public ReadIndex(File url){
        this.url = url;
    }
 
    public static void main(String[] args){
    	
		
    	
    	File file = new File("G:/index");
    
    	func(file);
		FileOutputStream output;
		try {

			output = new FileOutputStream("workbook.xls");
			wb.write(output);
			output.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}catch (IOException e) {
			// TODO: handle exception
		}
		

    }
 
    private static void func(File file) {
		File[] fs = file.listFiles();
		
		for(File f:fs){
			if(f.isDirectory())	
				func(f);
			if(f.isFile()&& f.getName().indexOf("index")!=-1){		
				
				ReadIndex app = new ReadIndex(f);
    	        app.run();
			
				}
		}
		

	}


    private static int table1(Document doc) {
        Elements trs = doc.select("table").select("tr");
        int i;
        boolean percent = false;
        int second = 1;
        for ( i=0; i<trs.size(); i++){
            Elements tds = trs.get(i).select("td");
           
           
            for (int j=0; j<tds.size(); j++){
                String txt = tds.get(j).text();
 
                if (txt.indexOf(".java")!=-1) {

                	System.out.print(txt.substring(0,txt.indexOf(".")));
                	String temp = txt.substring(0,txt.indexOf("."));
    			 //  	HSSFRow row = sheet.createRow(r);
                  
                   // 	HSSFCell cell=row.createCell(c);
                   
                    //	cell.setCellValue(temp);
                   // 	r++;
				//	c=1;
                	percent = true;
				}
                if (percent && txt.contains("%") && second ==1) {
					second = 2;
				}
                else if (percent && txt.contains("%") && second ==2) {
                	System.out.print(txt.substring(0,txt.indexOf("%"))+"% ");

                	HSSFRow row = sheet.createRow(r);
//                    
                	HSSFCell cell=row.createCell(c);
//               
                	cell.setCellValue(txt.substring(0,txt.indexOf("%")));
                	r++;
//                	c=0;
                	second = 1;
                	percent = false;
				}
               
            }
            System.out.println("");
        }
        return i;        
    }

	public void run() {
        Document doc;
        int rows;
	  try {
        doc = Jsoup.parse(url,"UTF-8","");
        // Page: 1
        rows = this.table1(doc);

	  } catch(IOException e) {
		e.printStackTrace();
	  }
    }
 
}