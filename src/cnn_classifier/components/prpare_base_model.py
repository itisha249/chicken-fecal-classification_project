import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from cnn_classifier.entity.config_entity import PrepareBaseModelConfig
from pathlib import Path



import tensorflow as tf
from pathlib import Path

class PrepareBasemodel:
    def __init__(self, config):
        self.config = config  # This should be an instance of PrepareBaseModelConfig

    def get_base_model(self):
        # Access properties directly from config without attempting to iterate
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.image_size,   # Adjust this according to your PrepareBaseModelConfig attributes
            weights=self.config.weights,          # Adjust this according to your PrepareBaseModelConfig attributes
            include_top=self.config.include_top   # Adjust this according to your PrepareBaseModelConfig attributes
        )
        self.save_model(path=self.config.base_model_path, model=self.model)

    def save_model(self, path, model):
        model.save(path)

    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif freeze_till is not None and freeze_till > 0:
            for layer in model.layers[:freeze_till]:
                layer.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in)

        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        full_model.summary()
        return full_model

    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )
        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)
