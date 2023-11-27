package com.example.prueba;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.app.Activity;
import android.os.Bundle;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;
import com.example.prueba.Adapter;
import com.example.prueba.R;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //Aquí va a ir el RecyclerView
        RecyclerView recyclerView = findViewById(R.id.recycler_view);
        Activity activity = this;
        JsonArrayRequest request = new JsonArrayRequest(
                Request.Method.GET,
                "https://raw.githubusercontent.com/fatimafernandezponte/DID/main/catalog.json",
                null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        //Aquí escribimos el código
                        //Iniciamos la variable List<AnimalitosData>
                        List<DataF>  allTheGatitos = new ArrayList<>();
                        for(int i = 0; i < response.length(); i++){
                            try{
                                JSONObject gatito = response.getJSONObject(i);
                                DataF data = new DataF(gatito);
                                allTheGatitos.add(data);
                            }catch(JSONException e){
                                e.printStackTrace();
                            }
                        }
                        Adapter adapter = new Adapter(allTheGatitos, activity);
                        recyclerView.setAdapter(adapter);
                        recyclerView.setLayoutManager(new LinearLayoutManager(activity));

                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Toast.makeText(activity, error.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                }

        );
        RequestQueue cola = Volley.newRequestQueue(this);
        cola.add(request);
    }


}