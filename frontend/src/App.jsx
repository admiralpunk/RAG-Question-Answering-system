import { useState } from 'react'
import FileUpload from './components/FileUpload'
import ChatInterface from './components/ChatInterface'
import { uploadPDF, askQuestion } from './services/api'
import './App.css'

function App() {
  const [file, setFile] = useState(null)
  const [docId, setDocId] = useState(null)
  const [messages, setMessages] = useState([])
  const [isProcessing, setIsProcessing] = useState(false)

  const handleFileUpload = async (uploadedFile) => {
    setFile(uploadedFile)
    setIsProcessing(true)
    
    try {
      const response = await uploadPDF(uploadedFile)
      setDocId(response.doc_id)
      setMessages([
        {
          type: 'system',
          text: `PDF "${uploadedFile.name}" has been processed and is ready for questions.`
        }
      ])
    } catch (error) {
      setMessages([
        {
          type: 'system',
          text: `Error processing PDF: ${error.message}`
        }
      ])
    } finally {
      setIsProcessing(false)
    }
  }

  const handleSendMessage = async (message) => {
    // Add user message
    setMessages(prev => [...prev, { type: 'user', text: message }])

    try {
      const response = await askQuestion(docId, message)
      setMessages(prev => [
        ...prev,
        {
          type: 'assistant',
          text: response.answer,
          citation: response.citation
        }
      ])
    } catch (error) {
      setMessages(prev => [
        ...prev,
        {
          type: 'system',
          text: `Error: ${error.message}`
        }
      ])
    }
  }

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <div className="max-w-4xl mx-auto bg-white rounded-lg shadow-lg overflow-hidden">
        <div className="p-6">
          <h1 className="text-2xl font-bold text-center mb-6">
            PDF Question-Answering System
          </h1>
          
          {!file && <FileUpload onFileUpload={handleFileUpload} />}
          
          {isProcessing && (
            <div className="text-center py-8">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto"></div>
              <p className="mt-4 text-gray-600">Processing PDF...</p>
            </div>
          )}
          
          {file && !isProcessing && (
            <div className="h-[600px]">
              <ChatInterface
                onSendMessage={handleSendMessage}
                messages={messages}
              />
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

export default App