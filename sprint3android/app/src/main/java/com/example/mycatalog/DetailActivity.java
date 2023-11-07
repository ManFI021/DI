package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.detail_activity);

        // Obtener referencias a los elementos de la interfaz de usuario
        TextView tituloTextView = findViewById(R.id.tituloTextView);
        ImageView imagenView = findViewById(R.id.imagenView);
        TextView descripcionTextView = findViewById(R.id.descripcionTextView);
        Button meGustaButton = findViewById(R.id.meGustaButton);
        meGustaButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Aquí puedes agregar el código para manejar el evento del botón "Me gusta".
            }
        });
        tituloTextView.setText("Pingu");
        descripcionTextView.setText("Sinceramente demuestra mi frustación con tantos trabajos de manera no proporcional a horas de sueño :)");
        imagenView.setImageResource(R.drawable.pingu);
    }
}