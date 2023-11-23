package com.example.myothercatalog;

import android.app.Activity;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

public class ImagenesViewHolder extends RecyclerView.ViewHolder {
    private ImageView imageView;
    private TextView nameTextView;

    public ImagenesViewHolder(View itemView) {
        super(itemView);
        imageView = itemView.findViewById(R.id.image_view);
        nameTextView = itemView.findViewById(R.id.text_view);
    }

    public void ShowData(DataModel data, Activity activity) {
        nameTextView.setText(data.getName());
        Glide.with(itemView.getContext()).load(data.getImageUrl()).into(imageView);
        System.out.print(data.getImageUrl());
    }
}

