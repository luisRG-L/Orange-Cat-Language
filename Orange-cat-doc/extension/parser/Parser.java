package extension.parser;

import extension.libs.*;

public class Parser {

    public static void parse(String textn, String ofile) {
        String[] lines = textn.split("\\n");
        StringBuilder html = new StringBuilder();

        html.append("<!DOCTYPE html>");
        html.append("<html>");

        for (String line: lines) {
            if (line.startsWith("! ")) {
                html.append("<title>").append(line.substring(2)).append("</title>");
            }else
            if(line.startsWith("$ ")) {
                html.append("<h1>").append(line.substring(2)).append("</h1>");
            }else
            if(line.startsWith("$$ ")) {
                html.append("<h2>").append(line.substring(3)).append("</h2>");
            }else
            if(line.startsWith("**")) {
                html.append("<strong>").append(line.substring(2, line.length() - 2)).append("</strong>");
            }else
            if(line.startsWith("/")) {
                html.append("<em>").append(line.substring(1, line.length() - 1)).append("</em>");
            }else
            if(line.startsWith("~")) {
                html.append("<del>").append(line.substring(1, line.length() - 1)).append("</del>");
            }else
            if(line.startsWith("_")) {
                html.append("<u>").append(line.substring(1, line.length() - 1)).append("</u>");
            }else
            if(line.startsWith(": \"")) {
                int index = line.indexOf("\"");
                String linkText = line.substring(1, index);
                String url = line.substring(index + 2, line.length() - 1);
                html.append("<a href=\"").append(url).append("\">").append(linkText).append("</a>");
            }else
            if(line.startsWith("_")) {
                int index = line.indexOf(" ");
                String language = line.substring(2, index);
                html.append("<pre><code class=\"").append(language).append("\">");
                // Read code block until the closing tag }
                StringBuilder codeBlock = new StringBuilder();
                while (!(line.endsWith("}")) ){
                    codeBlock.append(line).append("\n");
                }
                html.append(codeBlock).append("</code></pre>");
            }else
            if (line.startsWith("===")) {
                html.append("<hr>");
            }else
            if (line.startsWith("[")) {
                String filePath = line.substring(2, line.length() - 1);
                html.append("<img src=\"").append(filePath).append("\" />");
            }else
            html.append(line);
            html.append("<br>");
        }
        html.append("</html>");

        IO.createFile("docs/"+ofile+".html", html.toString());
    }
}
