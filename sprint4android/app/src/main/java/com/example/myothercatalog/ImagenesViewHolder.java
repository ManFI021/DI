package com.example.myothercatalog;

import android.app.Activity;
import android.content.Intent;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;


    // En ImagenesViewHolder.java
    public class ImagenesViewHolder extends RecyclerView.ViewHolder {
        private ImageView imageView;
        private TextView nameTextView;
        private Button btnDetail;

        public ImagenesViewHolder(View itemView) {
            super(itemView);
            imageView = itemView.findViewById(R.id.image_view);
            nameTextView = itemView.findViewById(R.id.text_view);
            btnDetail = itemView.findViewById(R.id.btn_detail);
        }

        public void ShowData(final DataModel data, final Activity activity) {
            nameTextView.setText(data.getName());
            Glide.with(itemView.getContext()).load(data.getImageUrl()).into(imageView);
            btnDetail.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    // Inicia la DetailActivity aquí
                    Intent intent = new Intent(activity, DetailActivity.class);
                    // Puedes pasar datos adicionales a la DetailActivity si es necesario
                    intent.putExtra("name", data.getName());
                    intent.putExtra("imageUrl", data.getImageUrl());
                    activity.startActivity(intent);
                }
            });
        }
    }



