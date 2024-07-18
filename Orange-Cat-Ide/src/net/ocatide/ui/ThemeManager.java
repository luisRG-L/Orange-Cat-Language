package net.ocatide.ui;

import java.awt.Color;
import java.awt.Font;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

import net.ocatide.interaction.UserInteraction;

@SuppressWarnings ("unused")
public class ThemeManager {
    public String modName; 
    
    public ThemeManager(){}

    public class Theme {
        public Color background_color,
                    foreground_color,
                    codearea_bg,
                    codearea_fg;
        public Font codeareaFont,
                    fileFont;

        public String themeName;

        public void load(){
            String completeDir = "assets/"+modName+"/config/themes/"+themeName+".properties";

            Properties properties = new Properties();
            try (FileInputStream fis = new FileInputStream(completeDir)){
                properties.load(fis);
            }catch(IOException e){
                new UserInteraction().alert(UserInteraction.AlertType.ERROR, "Cannot found app.properties");
            }

            String backgroundColorName = properties.getProperty("theme.color.background");
            String foregroundColorName = properties.getProperty("theme.color.foreground");

            String backgroundColorCodearea = properties.getProperty("theme.color.codearea.background");
            String foregroundColorCodearea = properties.getProperty("theme.color.codearea.foreground");

            String codeareaFontName = properties.getProperty("theme.font.codearea.name");
            String codeareaFontSize = properties.getProperty("theme.font.codearea.size");

            String fileFontName = properties.getProperty("theme.font.file.name");
            String fileFontSize = properties.getProperty("theme.font.file.size");
            

            background_color = Color.decode(backgroundColorName);
            foreground_color = Color.decode(foregroundColorName);

            codearea_bg = Color.decode(backgroundColorCodearea);
            codearea_fg = Color.decode(foregroundColorCodearea);

            int IcodeareaFontSize = Integer.valueOf(codeareaFontSize);
            int IfilesFontSize = Integer.valueOf(fileFontSize);

            codeareaFont = new Font(codeareaFontName, Font.PLAIN,  IcodeareaFontSize);
            fileFont = new Font(fileFontName, Font.PLAIN, IfilesFontSize);
        }
    }

    public List<Theme> themes = new ArrayList<>();

    public void registerTheme(String themeName){
        Theme thm = new Theme();
        thm.themeName = themeName;
        thm.load();
        themes.add(thm);
    }

    public Theme getTheme(String themeName){
        int i;
        for(i = 0; i < themes.size() - 1; i++){
            if (themes.get(i).themeName == themeName){
                break;
            }
        }
        return themes.get(i);
    }
}
