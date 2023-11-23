package com.example.myothercatalog;// MainActivity.java
import android.app.Activity;
import android.os.Bundle;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;
import com.example.myothercatalog.DataModel;
import com.example.myothercatalog.ImagenesAdapter;
import com.example.myothercatalog.R;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private RecyclerView recyclerView;
    private Activity activity;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        recyclerView = findViewById(R.id.recyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        activity = this;

        // URL del JSON de ejemplo
        String url = "https://raw.githubusercontent.com/ManFI021/DI/main/catalog.json";

        // Realiza la solicitud JSON usando Volley
        JsonArrayRequest jsonArrayRequest = new JsonArrayRequest(
                Request.Method.GET,
                url,
                null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                       List<DataModel> imagenes = new ArrayList<>();
                        try {
                            for (int i = 0; i < response.length(); i++) {
                                JSONObject jsonObject = response.getJSONObject(i);
                                DataModel dataModel = new DataModel(jsonObject);
                                imagenes.add(dataModel);
                            }
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                        ImagenesAdapter imagenesAdapter = new ImagenesAdapter(imagenes,activity);
                        recyclerView.setAdapter(imagenesAdapter);
                        recyclerView.setLayoutManager(new LinearLayoutManager(activity));

                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Toast.makeText(activity, error.getMessage(), Toast.LENGTH_SHORT).show();
                        error.printStackTrace();
                    }
                });

        // Agrega la solicitud a la cola
        // Inicializa la cola de solicitudes de Volley
        RequestQueue requestQueue = Volley.newRequestQueue(this);
        requestQueue.add(jsonArrayRequest);
    }
}
