package com.example.myothercatalog;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;

// En DetailActivity.java
public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.detail_acivity);

        // Recupera los datos de la intención
        Intent intent = getIntent();
        if (intent != null) {
            String name = intent.getStringExtra("name");
            String imageUrl = intent.getStringExtra("imageUrl");
            String description = intent.getStringExtra("description");

            // Muestra los datos en tu interfaz de usuario
            TextView nameTextView = findViewById(R.id.text_view);
            TextView descriptionTextView = findViewById(R.id.description_text_view);
            ImageView imageView = findViewById(R.id.image_view);

            if (nameTextView != null) {
                nameTextView.setText(name);
            }

            if (descriptionTextView != null) {
                descriptionTextView.setText(description);
            }

            if (imageView != null) {
                Glide.with(this).load(imageUrl).into(imageView);
            }
        }
    }
}
