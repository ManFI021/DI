package com.example.myothercatalog;

import com.android.volley.toolbox.JsonObjectRequest;

import org.json.JSONException;
import org.json.JSONObject;

public class DataModel {
    private String name;
    private String imageUrl;

    public DataModel(String name,String imageUrl) {
        this.name = name;
        this.imageUrl = imageUrl;
    }
    public DataModel(JSONObject json){
        try {
            this.name = json.getString("name");
            this.imageUrl = json.getString("image_url");
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
}
