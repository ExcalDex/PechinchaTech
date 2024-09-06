package br.cefet.pechinchatech.service;

import org.springframework.stereotype.Service;
import org.springframework.web.servlet.mvc.method.annotation.SseEmitter;

import br.cefet.pechinchatech.model.Produto;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

@Service
public class SseService {
    private final List<SseEmitter> emitters = new ArrayList<>();

    public SseEmitter inscrever() {
        SseEmitter emitter = new SseEmitter();
        emitters.add(emitter);
        emitter.onCompletion(() -> emitters.remove(emitter));
        emitter.onTimeout(() -> emitters.remove(emitter));
        return emitter;
    }

    public void notificarClientes(List<Produto> data) {
        List<SseEmitter> emittersMortos = new ArrayList<>();
        emitters.forEach(emitter -> {
            try {
                emitter.send(SseEmitter.event().data(data));
            } catch (IOException e) {
                emittersMortos.add(emitter);
            }
        });
        emitters.removeAll(emittersMortos);
    }
}
