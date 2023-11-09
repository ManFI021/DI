package com.example.mycatalog;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
public class DetailActivity extends AppCompatActivity {

    // Método onCreate se llama cuando se crea la actividad.
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        // Establecer el diseño de la actividad desde el archivo XML.
        setContentView(R.layout.detail_activity);
    }
}