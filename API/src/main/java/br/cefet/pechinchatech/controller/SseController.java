package br.cefet.pechinchatech.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.mvc.method.annotation.SseEmitter;

import br.cefet.pechinchatech.service.SseService;

@RestController
@RequestMapping("/api/sse")
@CrossOrigin(origins = "http://localhost:8100")
public class SseController {
    
    @Autowired
    private SseService sseService;

    @GetMapping("/inscrever")
    public SseEmitter inscreverParaNotificar() {
        return sseService.inscrever();
    }
}
