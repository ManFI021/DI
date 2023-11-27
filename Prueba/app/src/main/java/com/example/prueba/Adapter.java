package com.example.prueba;

import android.app.Activity;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.prueba.DataF;
import com.example.prueba.ViewHolder;

import java.util.List;

public class Adapter extends RecyclerView.Adapter<ViewHolder> {

    private List<DataF> allTheData;
    private Activity activity;



    //El método constructor del Adapter recibe una lista con todos los datos a cargar.
    public Adapter(List<DataF> dataset, Activity activity) {
        this.allTheData = dataset;
        this.activity = activity;
    }

    //Aquí creamos una celda.
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType){
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.viewholder, parent, false);
        //Aquí invocamos el constructor de AnimalitosViewHolder
        return new ViewHolder(view);
    }

    //Aquí le pasamos a la celda el contenido que debe mostrar según su posición, dependiendo de hasta dónde scrollee el usuario
    public void onBindViewHolder(ViewHolder holder, int position) {
        DataF dataIntPositionToBeRendered = allTheData.get(position);
        holder.showData(dataIntPositionToBeRendered, activity);
    }

        //Aquí devolvemos el número total de elementos de la lista
        @Override
        public int getItemCount () {
            return allTheData.size();
        }
    }
