If you want this code to run all the time, a good option would be to place it in a cloud system, such as pythonanywhere!


| Feature                       | Deprecated Java API 1.0                                 | New Java API 2.0 (This PR)                                |
|--------------------------------|------------------------------------------------------------|------------------------------------------------------------|
| **Load Model**                 | `CNNNetwork net = core.ReadNetwork(xmlPath)`             | `Model model = core.read_model(xmlPath)`                |
| **Compile Model**              | `ExecutableNetwork exec = core.LoadNetwork(net, device)`| `CompiledModel compiledModel = core.compile_model(model, device)` |
| **Inference Request**          | `execNetwork.CreateInferRequest()`                      | `compiledModel.create_infer_request()`                   |
| **Async Inference**            | `StartAsync()` & `Wait(WaitMode)`                       | `start_async()` & `wait_async()` (simplified)            |
| **Input Handling**             | Old-style `Blob`                                        | Modern `Tensor` object                                  |
| **Preprocessing**              | Verbose manual config                                   | Simplified via `PrePostProcessor` API                   |
| **Thread Management**          | Similar async threads                                   | Improved readability and robustness                     |
| **Visualization**              | OpenCV (unchanged)                                      | OpenCV (unchanged)                                      |

---
