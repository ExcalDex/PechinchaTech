package br.cefet.pechinchatech.controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.mvc.method.annotation.SseEmitter;

import br.cefet.pechinchatech.service.SseService;

@CrossOrigin
@RestController
@RequestMapping("/api/sse")
public class SseController {
    
    private final SseService sseService;

    public SseController(SseService sseService) {
        this.sseService = sseService;
    }

    @GetMapping("/subscribe")
    public SseEmitter inscreverParaNotificar() {
        return sseService.inscrever();
    }
}
