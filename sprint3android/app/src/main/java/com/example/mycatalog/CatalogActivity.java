package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class CatalogActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_catalog);

        Button btnOpenDetailActivity = findViewById(R.id.btnNavegarDetalle);
        btnOpenDetailActivity.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Aquí es donde lanzamos la actividad DetailActivity
                Intent intent = new Intent(CatalogActivity.this, DetailActivity.class);
                startActivity(intent);
            }
        });
    }
}