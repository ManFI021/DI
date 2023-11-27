package com.example.prueba;

import android.app.Activity;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import com.bumptech.glide.Glide;


import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

//Puede PUEDE que falte algo de Glide
public class ViewHolder extends RecyclerView.ViewHolder {
    private final TextView textView;
    private final ImageView imageView;

    //El método constructor recibe una View
    public ViewHolder(@NonNull View itemView) {
        super (itemView);
        textView = (TextView) itemView.findViewById(R.id.text_view); //TIENES QUE CREAR LAS MOVIDAS DEL XML
        imageView =(ImageView) itemView.findViewById(R.id.image_view);
    }

    //Este método recibe los datos a mostrar y una instancia tipo ACtivity
    //Se usa para pintar los datos y cargar la imagen
    public void showData(DataF data, Activity activity) {
        textView.setText(data.getName());
        Glide.with(itemView.getContext()).load(data.getImageUrl()).into(imageView);
    }
}
