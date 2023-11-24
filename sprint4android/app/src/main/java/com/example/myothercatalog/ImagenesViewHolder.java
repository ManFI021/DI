package com.example.myothercatalog;

import android.app.Activity;
import android.content.Intent;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

public class ImagenesViewHolder extends RecyclerView.ViewHolder {
    private ImageView imageView;
    private TextView nameTextView;
    private Button btnDetail;

    public ImagenesViewHolder(@NonNull View itemView) {
        super(itemView);
        imageView = itemView.findViewById(R.id.image_view);
        nameTextView = itemView.findViewById(R.id.text_view);
        btnDetail = itemView.findViewById(R.id.btn_detail);
    }

    public void ShowData(final DataModel data,Activity activity) {
        nameTextView.setText(data.getName());
        Glide.with(itemView.getContext()).load(data.getImageUrl()).into(imageView);

        if (btnDetail != null) {
            btnDetail.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    // Intenta iniciar la DetailActivity aquí
                    Intent intent = new Intent(activity, DetailActivity.class);

                    // Pasa los datos como extras
                    intent.putExtra("name", data.getName());
                    intent.putExtra("imageUrl", data.getImageUrl());
                    intent.putExtra("description",data.getDescription());

                    try {
                        // Asegúrate de que la actividad exista antes de iniciarla
                        activity.startActivity(intent);
                    } catch (Exception e) {
                        e.printStackTrace();
                        Toast.makeText(activity, "Error starting activity", Toast.LENGTH_SHORT).show();
                    }
                }
            });
        }
    }
}

