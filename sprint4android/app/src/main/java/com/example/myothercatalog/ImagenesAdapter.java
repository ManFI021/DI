package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class ImagenesAdapter extends RecyclerView.Adapter<ImagenesViewHolder> {
    private List<DataModel> imagenlist;
    private Activity activity;

    public ImagenesAdapter(List<DataModel> imagenlist, Activity activity) {
        this.imagenlist = imagenlist;
        this.activity = activity;
    }

    @NonNull
    @Override
    public ImagenesViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.imagenes_viewholder, parent, false);
        return new ImagenesViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ImagenesViewHolder holder, int position) {
        holder.ShowData(imagenlist.get(position),activity);
        DataModel dataModelPosition = imagenlist.get(position);
        holder.ShowData(dataModelPosition,activity);
    }

    @Override
    public int getItemCount() {
        return imagenlist.size();
    }
}
