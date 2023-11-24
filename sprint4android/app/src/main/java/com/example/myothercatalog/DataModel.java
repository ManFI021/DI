package com.example.myothercatalog;

import com.android.volley.toolbox.JsonObjectRequest;

import org.json.JSONException;
import org.json.JSONObject;

public class DataModel {
    private String name;
    private String imageUrl;

    private String description;

    public DataModel(String name,String imageUrl,String description) {
        this.name = name;
        this.imageUrl = imageUrl;
        this.description=description;
    }
    public DataModel(JSONObject json){
        try {
            this.name = json.getString("name");
            this.imageUrl = json.getString("image_url");
            this.description=json.getString("description");
        } catch (JSONException e){
            e.printStackTrace();
        }
    }

    public String getName() {
        return name;
    }

    public String getImageUrl() {
        return imageUrl;
    }

    public String getDescription(){return description;}
}
