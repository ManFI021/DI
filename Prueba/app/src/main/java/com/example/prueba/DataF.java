package com.example.prueba;

import org.json.JSONException;
import org.json.JSONObject;

public class DataF {
    private String name;
    private String imageUrl;


    public DataF(JSONObject json) {
        try {
            this.name = json.getString("name");
            this.imageUrl = json.getString("image_url");
        }catch (JSONException e){
            e.printStackTrace();
        }
    }

    public String getName(){return name;}
    public String getImageUrl(){return imageUrl;}
}