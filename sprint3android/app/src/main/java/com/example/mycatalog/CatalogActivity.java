package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

public class CatalogActivity extends Fragment {

    // Constructor.
    public CatalogActivity() {
    }

    //Crear la vista del fragmento.
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        // Inflar el layout.
        View rootView = inflater.inflate(R.layout.activity_catalog, container, false);
        Button buttonDetalle = rootView.findViewById(R.id.btnNavegarDetalle);
        buttonDetalle.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getActivity(), DetailActivity.class);
                startActivity(intent);
            }
        });
        return rootView;
    }
}